from .models import Application


# Create your controller here.


class EvaluationController(object):

    def __init__(self, application: Application=None, user=None):
        super().__init__()
        self.application = application
        self.user = user
        self.evaluations = list()
        self.process_evaluated_check()

    def process_evaluated_check(self):
        evaluations = self.evaluations
        application = self.application
        user = self.user
        for obj in application.get_application_applicant().prefetch_related():
            eval_dict = dict()
            eval_dict['applicant'] = obj.get_applicant()
            eval_dict['evaluated'] = obj.applicationevaluation_set.filter(user=user).count() > 0
            evaluations.append(eval_dict)

    def get_application_evaluation_states(self):
        return self.evaluations
