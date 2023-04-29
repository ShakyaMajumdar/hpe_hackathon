from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Option, Question, QuestionResult, Quiz

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "quizzes/index.html",
        context={
            "quizzes_list": Quiz.objects.all(),
        },
    )


class QuizView(View):
    def get(self, request: HttpRequest, quiz_id: int) -> HttpResponse:
        return render(
            request,
            "quizzes/quiz.html",
            context={"quiz": get_object_or_404(Quiz, id=quiz_id)},
        )

    def post(self, request: HttpRequest, quiz_id: int) -> HttpResponse:
        quiz_ = get_object_or_404(Quiz, id=quiz_id)

        selected_options: dict[Question, Option | None] = {}
        for i, question in enumerate(quiz_.questions.all(), start=1):  # type: ignore
            selected_option_id = request.POST.get(f"option{i}")
            selected_options[question] = (
                Option.objects.get(id=selected_option_id)
                if selected_option_id
                else None
            )

        question_results = [
            QuestionResult(
                question=question,
                selected_option=selected_option,
                correct_option=question.options.get(is_correct=True),  # type: ignore
            )
            for question, selected_option in selected_options.items()
        ]

        return render(
            request,
            "quizzes/results.html",
            context={
                "quiz": quiz_,
                "question_results": question_results,
            },
        )
