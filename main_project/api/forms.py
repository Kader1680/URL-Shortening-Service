# from django import forms 

# # class registerForm(forms.Form):
# #     username = forms.CharField(max_length = 200)
# #     email = forms.CharField(max_length = 200)
# #     passowrd = forms.CharField(widget = forms.PasswordInput()) 

# # from django.contrib.auth.models import User
# # from django import forms

# # class UserForm(forms.ModelForm):
# #     class Meta:
# #             model = User
# #             fields = [
# #                     'username', 
# #                     "passowrd"]
            
            
# class UserRegistrationForm(forms.ModelForm):
#     class Meta:
#             model = User
#             fields = [
#                     'username', 
#                     'email', 
#                     'passowrd',                     
#             ]