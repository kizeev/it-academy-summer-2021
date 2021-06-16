# Restaurant Tables

# In a small restaurant there are A tables for one person and B tables for two persons.
# It it known that N groups of people come today, each consisting of one or two people.
# If a group consist of one person, it is seated at a vacant one-seater table. If
# there are none of them, it is seated at a vacant two-seater table. If there are
# none of them, it is seated at a two-seater table occupied by single person. If
# there are still none of them, the restaurant denies service to this group.

# If a group consist of two people, it is seated at a vacant two-seater table. If
# there are none of them, the restaurant denies service to this group.

# You are given a chronological order of groups coming. You are to determine
# the total number of people the restaurant denies service to.

# Return the total number of people the restaurant denies service to.

def restaurant(single_tables, double_tables, visitors):
    lost_visitors = []
    half_double_tables = 0

    for i in visitors:
        if i == 1 and single_tables > 0:
            single_tables -= 1
        elif i == 1 and double_tables > 0:
            double_tables -= 1
            half_double_tables += 1
        elif i == 1 and half_double_tables > 0:
            half_double_tables -= 1
        elif i == 2 and double_tables > 0:
            double_tables -= 1
        else:
            lost_visitors.append(i)
    return sum(lost_visitors)
