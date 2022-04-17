import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Region, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()
    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])

        nums = [row[3], row[4], row[5], row[6]]

        for index, x in enumerate(nums):
            try:
                nums[index]= int(x)
            except:
                try:
                    nums[index] = float(x)
                except:
                    nums[index] = None

        s = Site(name= row[0], description=row[1], year=nums[0],
                latitude=nums[1], longitude=nums[2], area_hectares= nums[3],
                category = c, state= s, iso= i, region= r)

        s.save()
