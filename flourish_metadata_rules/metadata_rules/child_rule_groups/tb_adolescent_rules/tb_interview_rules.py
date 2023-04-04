from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRule, CrfRuleGroup, register, PF, P


app_label = 'flourish_child'


@register()
class TbAdolInterviewRuleGroup(CrfRuleGroup):

    transcription = CrfRule(
        predicate=P('interview_language', 'is not', None),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[
            f'{app_label}.tbadolinterviewtranscription',
        ])

    translation = CrfRule(
        predicate=PF('interview_language', func=lambda language: True if language ==
                     'setswana' or language == 'both' else False),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.tbadolinterviewtranslation'])

    class Meta:
        app_label = app_label
        source_model = f'{app_label}.tbadolinterview'
