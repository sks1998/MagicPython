a = 'blah {foo-bar %d'
a = 'blah {foo-bar %d}'
a = 'blah {foo-bar %d //insane {}}'
a = '{}blah {foo-bar %d //insane {}}'



a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
blah {foo-bar  : source.python, string.quoted.single.python
%d            : constant.character.format.python, source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
blah          : source.python, string.quoted.single.python
{foo-bar      : source.python, string.quoted.single.python
%d            : constant.character.format.python, source.python, string.quoted.single.python
}             : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
blah          : source.python, string.quoted.single.python
{foo-bar      : source.python, string.quoted.single.python
%d            : constant.character.format.python, source.python, string.quoted.single.python
 //insane {}} : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
a             : source.python
=             : keyword.operator.assignment.python, source.python
              : source.python
'             : punctuation.definition.string.begin.python, source.python, string.quoted.single.python
{}            : constant.character.format.python, source.python, string.quoted.single.python
blah          : source.python, string.quoted.single.python
{foo-bar      : source.python, string.quoted.single.python
%d            : constant.character.format.python, source.python, string.quoted.single.python
 //insane {}} : source.python, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.quoted.single.python
