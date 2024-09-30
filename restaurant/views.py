from django.shortcuts import render, redirect
import random
from django.http import HttpRequest, HttpResponse
import time

# Create your views here.

## restaurant/views.py - submit function
def submit(request):
    '''Process the form submission, and generate a result.'''
    template_name = "restaurant/confirmation.html"
    # read the form data into python variables:
    if request.POST:
         ##get the list of foods checked off by user
        chosen_foods = request.POST.getlist('food')
        chosen_foods = [food for food in chosen_foods if food != '0.00']
        ##if the list of chosen foods is empty, it will simply redirect to the order page
        if chosen_foods == []:
            return redirect('order')
        ##aquire necessary items from the post request
        name = request.POST['name']
        phone = request.POST['phone']
        meal_type = request.POST['dining_choice']
        ##initialize a variable to calculate the total price
        final_price = 0.0
        ##also initialize our tax for the food price
        tax = random.randint(2, 6)
        ##this for loop will iterate through the items and sum up the prices via float typecasting
        for item in chosen_foods:
            final_price = final_price + float(item)
        ##this is the final price with tax
        price_with_tax = final_price + tax
        ##below is formatting to make sure the floats are limited two decimal places 
        final_price = "{:.2f}".format(final_price)
        price_with_tax = "{:.2f}".format(price_with_tax)
        tax = "{:.2f}".format(float(tax))
        ###################################### the following lines are used to randomly calculate the ready time
        current_time = time.ctime()
        time_upd = time.time()
        update_time = time_upd + ((random.randint(30,60)) * 60)
        ready_time = time.localtime(update_time)
        format_time = time.strftime('%I:%M %p', ready_time)
        #######################################
        context = {
            'meal_type': meal_type,
            'name': name,
            'format_time':  format_time,
            'final_price': final_price,
            'taxed_price': price_with_tax,
            'tax': tax,
            'chosen_foods': chosen_foods,
            'phone': phone,
            'current_time': current_time,
            #'item_names': item_names,
        }
    else:
        return redirect('restaurant') #redirect to the restaurant if not a post request
    return render(request, template_name, context=context)


def order(request):
    '''Display the order page for the restaurant.'''
    template_name = "restaurant/order.html"
    # read the form data into python variables:
    special_items = ['Lasagna', 'Beef Stroganoff', 'Paella', 'Feijao Tropeiro']
    special_items_images = ['https://thecozycook.com/wp-content/uploads/2022/04/Lasagna-Recipe-f.jpg', 'https://i0.wp.com/www.therecipewench.com/wp-content/uploads/2016/11/Beef-stroganoff.jpg', 'https://tasteabroad.com/wp-content/uploads/2021/07/jjj.jpg', 'https://spiceworldinc.com/wp-content/uploads/2023/11/Feijoada-Scaled.jpg']
    special = random.randint(0, 3) #will choose the random item from the list
    context = {
        'current_time': time.ctime(),
        'special_item': special_items[special],
        'special_item_image': special_items_images[special],
        }
    return render(request, template_name, context=context)

def main(request):
    '''Display the main home page for the restaurant.'''
    template_name = "restaurant/main.html"
    # read the form data into python variables:
    #special_items = ['Lasagna', 'Beef Stroganoff', 'Paella', 'Feijao Tropeiro']
    #special_items_images = ['https://thecozycook.com/wp-content/uploads/2022/04/Lasagna-Recipe-f.jpg', 'https://i0.wp.com/www.therecipewench.com/wp-content/uploads/2016/11/Beef-stroganoff.jpg', 'https://tasteabroad.com/wp-content/uploads/2021/07/jjj.jpg', 'https://spiceworldinc.com/wp-content/uploads/2023/11/Feijoada-Scaled.jpg']
    #special = random.randint(0, 3) #will choose the random item from the list
    context = {
        'current_time': time.ctime(),
        #'special_item': special_items[special],
        #'special_item_image': special_items_images[special],
        }
    return render(request, template_name, context=context)