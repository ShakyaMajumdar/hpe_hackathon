from dataclasses import dataclass

from django.db import models

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false


class Quiz(models.Model):
    title = models.CharField(max_length=20)

    @property
    def num_questions(self) -> int:
        return len(self.questions.all())  # type: ignore

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    problem_statement = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.problem_statement


class Option(models.Model):
    option = models.CharField(max_length=50)
    is_correct = models.BooleanField()
    question = models.ForeignKey(
        Question, related_name="options", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return (
            f"{self.question} - {self.option}{' (Correct)' if self.is_correct else ''}"
        )


@dataclass
class QuestionResult:
    question: Question
    selected_option: Option | None
    correct_option: Option
