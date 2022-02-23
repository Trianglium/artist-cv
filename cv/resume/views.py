from django.shortcuts import render

# Create your views here.
def resume_index(request):
    template = loader.get_template('resume/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
