from apps.products.models import Products, Images, Categories
from django.views.generic import ListView,DetailView

class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['category'] = Categories.objects.all()
        return context

    def get_queryset(self):
        return Products.objects.all()

class ProductDetailView(DetailView):
    template_name = 'products/product_details.html'
    context_object_name = 'product_details'

    def get_object(self, queryset=None):
        products = Products.objects.get(pk=self.kwargs.get('pk'))
        similar = Categories.objects.filter(products=products)
        product1 = Products.objects.filter(category=similar[0])[:4]
        context =({'product': products, 'similer':product1 })
        return context

class ProductFilterView(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 8
    context_object_name = 'product_list'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductFilterView, self).get_context_data(*args, **kwargs)
        context['category'] = Categories.objects.all()
        return context

    def get_queryset(self):
        products = Products.objects.filter(category__id=self.kwargs.get('pk'))
        return products