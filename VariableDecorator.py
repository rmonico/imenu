#!/usr/bin/python3
# coding: utf-8

from unittest import TestCase, skip, main as unittest_main


class VariableDecorator(object):

    def __init__(self, variables):
        pass

    def expand(self, format):
        return 'variable value'


class TestSomething(TestCase):

    # ?:variable?
    # ?prefixo:variable?
    # ?variable::sufixo?
    # ?variable??if null::Variable not defined?
    # ?variable??if null or empty::Variable not defined?

    # ?[prefixo:]variable[::sufixo][??expression::valor se true]?

    # expression: if [nulo [or empty] | [ empty ] ]
    def test_should_expand_variable(self):
        decorator = VariableDecorator({'variable': 'variable value'})

        generated_value = decorator.expand('?:variable?')

        self.assertEqual(generated_value, 'variable value')

    @skip('Not implemented yet')
    def test_should_expand_variable_with_prefix(self):
        decorator = VariableDecorator({'variable': 'variable value'})

        generated_value = decorator.expand('?prefix - :variable?')

        self.assertEqual(generated_value, 'prefix - variable value')

    # @skip('Not implemented yet')
    # def test_should_expand with_suffix(self):
    #     decorator = VariableDecorator({'variable': 'variable value'})

    #     generated_value = decorator.expand('?:variable:: - suffix?')

    #     self.assertEqual(generated_value, 'variable value - suffix')

    # @skip('Not implemented yet')
    # def test_should_expand with_expression(self):
    #     decorator = VariableDecorator({'variable': 'variable value'})

    #     generated_value = decorator.expand('?:variable if undefined,null,empty :not defined; if ')

    #     generated_value = decorator.expand('?:variable ;? undefined :variable not defined; if null :variable is null; case empty :variable is empty;')

    #     self.assertEqual(generated_value, 'variable value - suffix')


if __name__ == '__main__':
    unittest_main()
