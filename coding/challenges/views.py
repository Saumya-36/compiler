# challenges/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Challenge, Submission, TestCase
from .compiler import CCodeCompiler

def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/challenge_list.html', {'challenges': challenges})

def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    test_cases = TestCase.objects.filter(challenge=challenge)
    return render(request, 'challenges/challenge_detail.html', {'challenge': challenge, 'test_cases': test_cases})

def submit_code(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    test_cases = TestCase.objects.filter(challenge=challenge)

    if request.method == 'POST':
        user_code = request.POST.get('code', '')
        compiler = CCodeCompiler()

        # Initialize result as a list to store results for each test case
        results = []

        try:
            # Evaluate the code against each test case
            for test_case in test_cases:
                result = compiler.compile_with_test_case(user_code, test_case.input_data)

                # Store the result along with the test case information
                results.append({'test_case': test_case.id, 'result': result})

            # Save submission result to the database
            submission = Submission(challenge=challenge, user_code=user_code)
            submission.save()

            # Return JSON response with results
            return JsonResponse({'results': results})

        except Exception as e:
            # Handle exceptions during compilation or execution
            return JsonResponse({'error': str(e)}, status=500)

    # Handle GET requests or other methods
    return JsonResponse({'error': 'Invalid request method'}, status=400)
