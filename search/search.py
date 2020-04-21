from .models import SearchTerm
from django.db.models import Q
from blog.models import Post

STRIP_WORDS = ['a', 'an', 'and', 'by', 'for', 'from', 'in', 'no', 'not', 'of', 'on', 'or', 'that', 'the', 'to', 'with']


# strip out common words, limit to 5 words
def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]


# store the search text in the database
def store(request, q):
    # if search term is at least three chars long, store in db
    if len(q) > 2:
        term = SearchTerm()
        term.q = q
        term.ip_address = request.META.get('REMOTE_ADDR')
        term.user = None
        if request.user.is_authenticated():
            term.user = request.user
            term.save()


# get products matching the search text
def post(search_text):
    words = _prepare_words(search_text)
    posts = Post.objects.all()
    results = {}
    # iterate through keywords
    for word in words:
        # Search in title, or body
        posts = posts.filter(Q(title__icontains=word) | Q(body__icontains=word))
        #results['items'] = posts
        return posts
