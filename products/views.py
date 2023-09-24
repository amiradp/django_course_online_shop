from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Comment, Category
from .forms import CommentForm
from cart.forms import AddToCartProductForm


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id=product_id)

        obj.product = product

        return super().form_valid(form)


def category_view(request, cats):
    category_post = Product.objects.filter(category=cats)
    return render(request, 'products/category_list.html', {
        'cats': cats.title(),
        'category_post': category_post,
    })


def search_product(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Product.objects.filter(title__contains=searched)

        return render(request, 'products/search_venues.html', {'searched': searched,
                                                               'venues': venues
                                                               })
    else:
        return render(request, 'products/search_venues.html', {})


class ProductCategoryView(generic.ListView):
    model = Product
    template_name = 'products/product_category_list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ProductCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
