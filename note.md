Commands: <br/>
```bin
python manage.py sql migrate polls 001
#this command take migration names and return their sql

#output
BEGIN;
--
-- Create model Questions
--
CREATE TABLE "polls_questions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_questions" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```
---
```bin
python3 manage.py shell
#this opens an interactive shell for the project

#if you want to query or test the models import the models app first
from polls.models import Questions
Questions.objects.all()

#Output
<QuerySet []>

```

---
```bin

Questions.objects.filter(question_text__startswith-"What")

#this will return the objects that start with string "What"

q = Questions.objects.get(pk=1)
#will return an object with id == 1

q.choice_set.all()
#this will return all the objects in Choice that is related to Question or have a foreign key == to the id of the Questions

#Output
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

```

---
```bin
q.choice_set.create(choice_text="Not much", votes=0)
#creating an object with realtionship to object of q(Question object with the id of 1)
```


