#!/usr/bin/env python3
"""
Band Name Generator
A simple, interactive console application to generate a creative band name
based on user-provided input.
"""

def get_user_input(prompt: str) -> str:
    """
    Prompt the user for input and return the stripped response.
    """
    return input(prompt).strip()

def generate_band_name(city: str, pet_name: str) -> str:
    """
    Generate a band name by combining the city and pet name.
    """
    return f"{city} {pet_name}"

def main():
    """
    Main entry point for the Band Name Generator application.
    """
    print("Welcome to the Band Name Generator!\n")

    city = get_user_input("Enter the city you grew up in: ")
    pet = get_user_input("Enter your pet's name: ")

    band_name = generate_band_name(city, pet)
    print(f"\nYour band name could be: {band_name}")

if __name__ == "__main__":
    main()
