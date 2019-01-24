from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import randrange


@api_view()
def d2(request):
    """Throw a D2
    """
    return Response({"result": randrange(1, 3)})


@api_view()
def d4(request):
    """Throw a D4
    """
    return Response({"result": randrange(1, 5)})


@api_view()
def d6(request):
    """Throw a D6
    """
    return Response({"result": randrange(1, 7)})


@api_view()
def d8(request):
    """Throw a D8
    """
    return Response({"result": randrange(1, 9)})


@api_view()
def d10(request):
    """Throw a D10
    """
    return Response({"result": randrange(1, 11)})


@api_view()
def d12(request):
    """Throw a D12
    """
    return Response({"result": randrange(1, 13)})


@api_view()
def d20(request):
    """Throw a D20
    """
    return Response({"result": randrange(1, 21)})


@api_view()
def d100(request):
    """Throw a D100
    """
    return Response({"result": randrange(1, 101)})
