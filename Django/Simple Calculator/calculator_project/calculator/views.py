from django.shortcuts import render

# Create your views here.
def calculator(request):
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2
        except(ValueError,ZeroDivisionError) as e:
            result = "Error:"+str(e)
    return render(request,'calculator/calculator.html',{'result':result})
    