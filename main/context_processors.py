from main.models import Author

# Context Processors to add data to all pages


def author_processor(request):

    author = Author.objects.first()
    return{'author': author}
