from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):
    products = [
        {
            'name': 'Laptop',
            'price': 55000,
            'category': 'Electronics'
        },
        {
            'name': 'Mobile',
            'price': 20000,
            'category': 'Electronics'
        },
        {
            'name': 'T-Shirt',
            'price': 800,
            'category': 'Clothing'
        }
    ]

    return Response(products)
