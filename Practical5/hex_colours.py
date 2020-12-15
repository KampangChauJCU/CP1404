COLOUR = {"AliceBlue": "#f0f8ff", "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd",
          "azure4": "#838b8b", "beige": "#f5f5dc", "bisque1": "#eed5b7", "bisque3": "#cdb79e",
          "bisque4": "#8b7d6b", "BlanchedAlmond": "#ffebcd"}

colour_name = input("Enter the name:")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR.get(colour_name)))
    colour_name = input("Enter the name:")
