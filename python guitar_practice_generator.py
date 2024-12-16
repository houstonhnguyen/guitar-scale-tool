import random

class GuitarPracticeGenerator:
    def __init__(self):
        # Define all possible keys
        self.keys = [
            'C', 'Db', 'D', 'Eb', 'E', 'F', 
            'Gb', 'G', 'Ab', 'A', 'Bb', 'B'
        ]
        
        # Define possible scales
        self.scales = [
            'Major', 'Dorian', 'Phrygian', 'Lydian', 
            'Mixolydian', 'Aeolian', 'Locrian', 
            'Minor Pentatonic', 'Major Pentatonic'
        ]
        
        # Define possible arpeggios
        self.arpeggios = [
            'Minor Triad', 'Major Triad', 
            'Augmented Triad', 'Diminished Triad', 
            'Minor 7th', 'Major 7th', 
            'Dominant 7th', 'Minor 7th Flat 5', 
            'Diminished 7th'
        ]
    
    def generate_exercise(self, include_arpeggios=False):
        """
        Generate a random guitar practice exercise.
        
        :param include_arpeggios: If True, includes arpeggios in possible options
        :return: A tuple containing the key, pattern, and exercise type
        """
        # Randomly select a key
        key = random.choice(self.keys)
        
        # Randomly select a CAGED pattern (1-5)
        pattern = random.randint(1, 5)
        
        # Determine whether to generate a scale or arpeggio
        if include_arpeggios:
            exercise_type = random.choice(self.scales + self.arpeggios)
        else:
            exercise_type = random.choice(self.scales)
        
        return key, pattern, exercise_type
    
    def generate_multiple_exercises(self, num_exercises=5, include_arpeggios=False):
        """
        Generate multiple random guitar practice exercises.
        
        :param num_exercises: Number of exercises to generate
        :param include_arpeggios: If True, includes arpeggios in possible options
        :return: A list of exercises
        """
        exercises = []
        for _ in range(num_exercises):
            exercises.append(self.generate_exercise(include_arpeggios))
        return exercises

def main():
    # Create an instance of the generator
    generator = GuitarPracticeGenerator()
    
    # Generate 5 exercises without arpeggios
    print("5 Scale Exercises:")
    scale_exercises = generator.generate_multiple_exercises(5, include_arpeggios=False)
    for key, pattern, scale in scale_exercises:
        print(f"{key} Pattern {pattern} - {scale}")
    
    print("\n5 Exercises (including arpeggios):")
    mixed_exercises = generator.generate_multiple_exercises(5, include_arpeggios=True)
    for key, pattern, exercise in mixed_exercises:
        print(f"{key} Pattern {pattern} - {exercise}")
    
    # Interactive mode
    while True:
        print("\nGuitar Practice Generator")
        print("1. Generate Scale Exercises")
        print("2. Generate Mixed Exercises (Scales and Arpeggios)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            num = int(input("How many exercises would you like? "))
            exercises = generator.generate_multiple_exercises(num, include_arpeggios=False)
            print("\nGenerated Exercises:")
            for key, pattern, scale in exercises:
                print(f"{key} Pattern {pattern} - {scale}")
        
        elif choice == '2':
            num = int(input("How many exercises would you like? "))
            exercises = generator.generate_multiple_exercises(num, include_arpeggios=True)
            print("\nGenerated Exercises:")
            for key, pattern, exercise in exercises:
                print(f"{key} Pattern {pattern} - {exercise}")
        
        elif choice == '3':
            print("Goodbye! Keep practicing!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
