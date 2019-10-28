class A(object):
    def __init__(self):
        print('Enter A')
    def _pMethod(self):
        print('MethodA')

class B(A):
    def __init__(self):
        print('Enter B')
        A.__init__(self)

    def _pMethod(self):
        print ('MethodB')

b=B()
b._pMethod()
