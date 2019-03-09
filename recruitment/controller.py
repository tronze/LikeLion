from .models import Application, ApplicationEvaluation, AnswerEvaluation


# Create your controller here.


class EvaluationController(object):

    def __init__(self, application: Application=None, user=None):
        super().__init__()
        self.application = application
        self.user = user
        self.evaluations = list()

    def process_evaluated_check(self):
        evaluations = self.evaluations
        application = self.application
        user = self.user
        if application is not None and user is not None:
            for obj in application.get_application_applicant().prefetch_related():
                eval_dict = dict()
                eval_dict['applicant'] = obj.get_applicant()
                eval_dict['evaluated'] = obj.applicationevaluation_set.filter(user=user).count() > 0
                eval_dict['application_pk'] = obj.pk
                evaluations.append(eval_dict)

    def process_evaluated_data(self):
        evaluations = self.evaluations
        application = self.application
        user = self.user
        if application is not None and user is not None:
            for obj in application.get_application_applicant().prefetch_related():
                eval_dict = dict()
                eval_dict['applicant'] = obj.get_applicant()
                scores = list()
                # try:
                #     answers = obj.get_applicant().answer_set.order_by('question__order')
                #     for answer in answers:
                #         try:
                #             application_evaluation = obj.applicationevaluation_set.get(user=user)
                #             evaluated = answer.answerevaluation_set.get(application_evaluation=application_evaluation)
                #             score = evaluated.score
                #         except ApplicationEvaluation.DoesNotExist:
                #             score = None
                #         except AnswerEvaluation.DoesNotExist:
                #             score = None
                #         scores.append(score)
                # except ApplicationEvaluation.DoesNotExist:
                #     eval_dict['scores'] = None
                try:
                    questions = self.get_questions()
                    for question in questions:
                        try:
                            application_evaluation = obj.applicationevaluation_set.get(user=user)
                            evaluated = question.answer_set.get(applicant=obj.get_applicant()).answerevaluation_set.get(application_evaluation=application_evaluation)
                            score = (question.order, evaluated.score)
                        except ApplicationEvaluation.DoesNotExist:
                            score = (question.order, None)
                        except AnswerEvaluation.DoesNotExist:
                            score = (question.order, None)
                        scores.append(score)
                except ApplicationEvaluation.DoesNotExist:
                    eval_dict['scores'] = None
                eval_dict['scores'] = scores
                eval_dict['pk'] = obj.pk
                evaluations.append(eval_dict)

    def get_questions(self):
        return self.application.question_set.order_by('order')

    def get_application_evaluation_states(self):
        return self.evaluations
