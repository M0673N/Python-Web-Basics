from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def pet_all(request):
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    likes = pet.like_set.count()
    context = {'pet': pet, 'likes': likes}
    return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('pet details', pet.id)
