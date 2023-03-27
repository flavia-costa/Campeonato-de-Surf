def winners(name, points):
    winners_list = []
    highest_points = []
    for x in range(3):
        y = points.index(max(points))
        highest_points.append(points[y])
        winners_list.append(name[y])
        name.pop(y)
        points.pop(y)

    return winners_list, highest_points

print('-'*44)
print('Ranking System - Surf Championship')
print('-'*44)

competitors = []
scores = []
counter = 1

while True:
    competitor = input('Enter the competitor\'s name: ')
    while counter != 0:
        try:
            competitor_points = int(input('Enter the competitor\'s final score: '))
            counter = scores.count(competitor_points)
            if counter == 0:
                scores.append(competitor_points)
                competitors.append(competitor)
            else:
                print('\nThe system does not allow two equal scores to be recorded. There are no ties in this tournament.')
        except ValueError:
            print('\nInvalid input. Please enter a numerical score.')
    counter = 1
    proceed = input('\nDo you want to make a new registration? Enter (Y/N)').upper()
    if proceed != 'Y':
        break

winners, highest_scores = winners(competitors, scores)
print('\nRanking: ')
for x in range(3):
    print(f'{x+1}º place: {winners[x]} - {highest_scores[x]} Points')
