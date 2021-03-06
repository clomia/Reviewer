from django.shortcuts import render, redirect
from . import models as book_model
from core.custom_package import (
    sorted_cut,
    sort_by_total_rating,
    sorted_by_total_rating_form_review,
)

# Create your views here.


def book_main(request):
    page = int(request.GET.get("page", 1) or 1)
    # 말 그대로 request를 GET 메소드로 받아낸다 QueryDict으로 가공된것을 넘겨받는다
    # QueryDict.get()을 사용할수 있따 dir(QueryDict)로 본다
    page_size = 20
    page_count = int(book_model.Book.objects.count() / page_size) + 1
    limit = page_size * page
    offset = limit - page_size
    books = sorted_cut(book_model.Book, "year", offset, limit)
    set_books = sort_by_total_rating(books)
    set_review = [sorted_by_total_rating_form_review(book[1], 5) for book in set_books]
    # 가로5 X 세로4 로 배치, Nav는 수직으로 세워서 배치

    return render(
        request,
        "books/main.html",
        {
            "book_data": zip(set_books, set_review),
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )


def book_detail(request, pk):
    page = int(request.GET.get("page", 0) or 0)
    # 일단은 리뷰 더보기 기능으로 생각
    model = book_model.Book.objects.get(pk=pk)
    total_rating = model.total_rating()
    reviews = model.review_set.all()
    page_size = 20
    main_page_size = 5
    page_count = int((book_model.Book.objects.count() - main_page_size) / page_size)
    limit = (page * page_size) + main_page_size
    offset = limit - page_size if limit > main_page_size else 0
    review_data = reviews.order_by("-rating")[offset:limit]
    return render(
        request,
        "books/detail.html",
        {
            "book": model,
            "total_rating": total_rating,
            "page_count": page_count - 1,
            "page_range": range(page_count),
            "review_data": review_data,
            "page": page,
        },
    )
