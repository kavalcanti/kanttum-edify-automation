grades = []
criteria_str = ['Form URL:',
           'The lesson was effectively customized.',
           'The teacher had all necessary materials/links ready before the start of the lesson.',
           'The online classroom background was appropriate to Ss.',
           'The teacher made use of extra resources in a meaninful way.',
           'The teacher was able to establish sufficient rapport.',
           'The teacher signposted learning objectives.',
           'The teacher used contextualization and elicitation techniques.',
           'The teacher presented langauge/content effectively.',
           'Instructions were short and clear.',
           'The teacher offered opportunities for practice.',
           'The teacher offered opportunities for meaningful and relevant conversation.',
           'The teacher offered opportunities for collaboration.',
           'The teacher varied the pace to foster learning.',
           'The teacher personalized learning.',
           'The teacher exploited emergent language.',
           'The teacher promoted a sense of progress.',
           'The teacher made effective use of scaffolding strategies.',
           'The teacher managed time well.',
           'Ss interacted with each other and the teacher.',
           'Ss asked questions.',
           'Ss were engaged.',
           'Ss produced the expected language.',
           'The teacher showed good command of the language.',
           'The teacher used appropriate language for the level/group.',
           'The teacher met the lesson objectives.',
           'Strengths.',
           'Suggestions for improvement.']
#dados de login
email_mentor = input('E-mail cadastrado: ')
senha_mentor = input('Senha: ')
#coleta das notas.
print('Hit ENTER for Not Applicable.')
for criterion in criteria_str:
    add = input('{}'.format(criterion))
    grades.append(converter_notas(add))
