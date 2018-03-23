# Without changing the provided lists and dictionaries, create a script that cycles
# through all the parents and prints to the terminal the proper activities for
# their child's age group. When there are no more activities for that parent,
# print “curriculum complete!” and move on to the next parent.
#
# (Make sure your script accounts for any edge cases in the provided variables!)

parents = [
    {'parent': 'Henry', 'child': {'name': 'Calvin', 'age': 2}},
    {'parent': 'Ada', 'child': {'name': 'Lily', 'age': 3}},
    {'parent': 'Emilia', 'child': {'name': 'Petra', 'age': 1}},
    {'parent': 'Biff', 'child': {'name': 'Biff Jr', 'age': 4}},
    {'parent': 'Milo', 'child': {}}
]

curriculum = [
    {
        'age': 1,
        'activity': [
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Go outside and feel surfaces.',
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Personalize the message output to make it more friendly.
# - Allow users to input new activities & parents before executing the script.
# - Print one activity at a time per parent and continue cycling through until
#   all parents have recieved all their activities.

#################################
#MY IMPLEMENTATION OF THE SCRIPT#
#################################

#compares age of child and age values presented in the curriculum list
#then for each child, presents a curriculum corresponding to their age
#also checks for parents with no children in the system and those who have
#children whose age does not fall in the range 1-3
def curriculumFinder():
    agelist=[];
    for curriculumAge in curriculum:
        agelist.append(curriculumAge['age']);
    for curriculumAge in parents:
        if not curriculumAge['child']:
            print("Hello " + curriculumAge['parent'] + " You have no kids so we are unable to provide a curriculum!")
        else:
            print('Hello '+ curriculumAge['parent']+ '! The name of your child that we have on record is: ' + curriculumAge['child']['name'] + " who is " + str(curriculumAge['child']['age']) + " years old!")
            childAge=curriculumAge['child']['age']
            if childAge in agelist:
                print("Your curriculum is:")
                for index in agelist:
                    if childAge == agelist[index-1]:
                        for curriculumRecommendation in curriculum[index-1]['activity']:
                            print(curriculumRecommendation)
                print('Curriculum Complete!')
            else:
                print("Your child is not 1-3 years old so we are currently unable to provide a curriculum. Sorry for the inconvinience! Please Check back in the near future!")
        print()

curriculumFinder();
