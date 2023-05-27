from django_cron import CronJobBase, Schedule
from datetime import datetime
from quiz_api.models import Quiz

class UpdateQuizStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'quiz_app.update_quiz_status_cron_job'  

    def do(self):
        now = datetime.now()
        active_quizzes = Quiz.objects.filter(start_date__lte=now, end_date__gte=now)
        finished_quizzes = Quiz.objects.filter(end_date__lt=now)

        for quiz in active_quizzes:
            quiz.status = 'active'
            quiz.save()

        for quiz in finished_quizzes:
            quiz.status = 'finished'
            quiz.save()
            


