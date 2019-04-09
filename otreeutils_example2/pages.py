# Definition of views/pages for the survey.
# Please note: When using oTree 2.x, this file should be called "pages.py" instead of "views.py"
#

from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from otreeutils.surveys import SurveyPage, setup_survey_pages


class SurveyIntro(Page):
    pass


# let's create the survey pages here
# unfortunately, it's not possible to create them dynamically


class SurveyPage1(SurveyPage):
    pass


class SurveyPage2(SurveyPage):
    pass


class SurveyPage3(SurveyPage):
    pass


class SurveyPage4(SurveyPage):
    pass


class SurveyPage5(SurveyPage):
    def get_context_data(self, **kwargs):
#        del kwargs['form'].fields['q_treatment_%d' % remove_form]
        ctx_data = super().get_context_data(**kwargs)

        if self.player.treatment == 1:
            remove_form = 2
        else:
            remove_form = 1

        del ctx_data['survey_forms']['treatment_%d_form' % remove_form]

        return ctx_data


# Create a list of survey pages.
# The order is important! The survey questions are taken in the same order
# from the SURVEY_DEFINITIONS in models.py

survey_pages = [
    SurveyPage1,
    SurveyPage2,
    SurveyPage3,
    SurveyPage4,
    SurveyPage5,
]

# Common setup for all pages (will set the questions per page)
setup_survey_pages(models.Player, survey_pages)

page_sequence = [
    SurveyIntro,
]

# add the survey pages to the page sequence list
page_sequence.extend(survey_pages)