Here is a **clean, stylized, readable Markdown version** of your notes — structured, formatted, and made visually clearer:

---

# 📘 Django & DRF Notes – Clean & Stylized

---

## 🧱 Migrations: View SQL Output

```bash
python manage.py sqlmigrate polls 001
```

📌 Shows the SQL statements Django will run for migration `001`.

### ✅ Example Output

```sql
BEGIN;
-- Create model Questions
CREATE TABLE "polls_questions" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "question_text" varchar(200) NOT NULL,
    "pub_date" datetime NOT NULL
);

-- Create model Choice
CREATE TABLE "polls_choice" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" bigint NOT NULL REFERENCES "polls_questions" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX "polls_choice_question_id_c5b4b260"
    ON "polls_choice" ("question_id");
COMMIT;
```

---

## 🐍 Django Shell Examples

```bash
python3 manage.py shell
```

### Import the model

```python
from polls.models import Questions
Questions.objects.all()
```

### QuerySet output

```python
<QuerySet []>
```

---

## 🔍 Model Queries

### Filter objects starting with `"What"`

```python
Questions.objects.filter(question_text__startswith="What")
```

### Get by primary key

```python
q = Questions.objects.get(pk=1)
```

### Access related objects via foreign key

```python
q.choice_set.all()
```

✅ Output:

```python
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
```

---

## ➕ Create a related Choice

```python
q.choice_set.create(choice_text="Not much", votes=0)
```

---

## 🔄 Difference Between `request.POST` & `request.data`

```python
request.POST  # Only handles form data, only works on POST
request.data  # Handles JSON, form, multipart, works on POST/PUT/PATCH
```

---

# ⚙️ DRF: Customizing Generic Views

## ✅ Customize CREATE behavior

```python
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

---

## ✅ Customize UPDATE behavior

```python
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_update(self, serializer):
        if "title" in serializer.validated_data and serializer.validated_data["title"] == "":
            raise ValidationError("Title cannot be empty")
        serializer.save(updated_by=self.request.user)
```

---

## ✅ Customize DELETE behavior

```python
def perform_destroy(self, instance):
    print(f"Snippet {instance.id} deleted by {self.request.user}")
    instance.delete()
```

---

## ✅ Override `create()` for advanced control

### Access raw data

```python
def create(self, request, *args, **kwargs):
    print("Raw data:", request.data)
    return super().create(request, *args, **kwargs)
```

### Custom validation

```python
def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.validated_data.get("title") == "forbidden":
        return Response({"error": "Invalid title"}, status=400)

    self.perform_create(serializer)
    return Response(serializer.data, status=201)
```

---

## ✅ Override `update()` for advanced update flow

```python
def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()

    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)

    if serializer.validated_data.get("title") == "hack":
        return Response({"error": "Hacking the title is not allowed"}, status=403)

    self.perform_update(serializer)
    return Response(serializer.data)
```

---

# 📌 Summary Table: When to Override

| Method              | When to Use                        |
| ------------------- | ---------------------------------- |
| `perform_create()`  | Add extra fields (owner), logging  |
| `perform_update()`  | Custom validation, computed fields |
| `perform_destroy()` | Logging, soft delete               |
| `create()`          | Manual control, custom responses   |
| `update()`          | Deep customization, logic checks   |

---


