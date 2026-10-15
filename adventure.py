scenes = [
    ("You enter the park beneath a bright spring sky. A path splits ahead.", [
        ("Take the shady path by the pond.", 1),
        ("Follow a jogger toward the garden.", 1),
        ("Wander after a drifting kite.", 0),
    ]),
    ("Near the pond, you spot a scarf on a bench and a duckling in the reeds.", [
        ("Give the scarf to the park keeper.", 1),
        ("Wait nearby in case someone comes back for it.", 1),
        ("Keep walking and enjoy the birdsong.", 0),
    ]),
    ("The sun begins to set as you reach a little wooden bridge.", [
        ("Help a family find their way back to the entrance.", 1),
        ("Sit on the bridge and watch the sunset.", 0),
        ("Take one last loop around the flower beds.", 0),
    ]),
]

kind_choices = 0
garden_route = False
print("THE PARK WALK\n")

for step, (scene, options) in enumerate(scenes, 1):
    if step == 2 and garden_route:
        scene = "In the garden, the jogger pauses beside a bed of drooping flowers."
        options = [
            ("Help water the flowers.", 1),
            ("Ask the gardener about the bright tulips.", 1),
            ("Follow the garden path toward the bridge.", 0),
        ]
    print(f"Step {step}: {scene}")
    for number, (option, _) in enumerate(options, 1):
        print(f"  {number}. {option}")
    while True:
        answer = input("Choose 1, 2, or 3: ").strip()
        if answer in ("1", "2", "3"):
            break
        print("Please enter 1, 2, or 3.")
    kind_choices += options[int(answer) - 1][1]
    if step == 1:
        garden_route = answer == "2"
    print()

if kind_choices >= 2:
    print("Ending 1: Your small kindnesses brighten the park and your walk home.")
else:
    print("Ending 2: You leave the park refreshed, carrying the sunset's quiet with you.")