import cgi
import os

# Create the plist file and write opening structure
output = open("PokemonIVTextSub.plist", "w")
output.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
output.write(
    "<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n")
output.write("<plist version=\"1.0\">\n")
output.write("<array>\n")
# Grabs files in project directory
IVTypes = sorted(os.listdir("."))
for ivType in IVTypes:
    # Using only the folders with IV strings
    if ivType.endswith("strings"):
        IVFolder = sorted(os.listdir(ivType + "/"))
        for gen in IVFolder:
            # Creates list of all Pokemon in Gen folder
            pokemonIVFiles = sorted(os.listdir(ivType + "/" + gen + "/"))
            for pokemon in pokemonIVFiles:
                input_pokemon = open(ivType + "/" + gen + "/" + pokemon)
                pokemonCPString = cgi.escape(input_pokemon.readline())
                input_pokemon.close()
                # Gets Pokemon name
                if pokemon.split()[0] != "029" and pokemon.split()[0] != "032":
                    pokemonName = pokemon.split()[-1].lower()
                elif pokemon.split()[0] == "029":
                    pokemonName = pokemon.split()[2].lower() + "f"
                else:
                    pokemonName = pokemon.split()[2].lower() + "m"
                output.write("\t<dict>\n")
                output.write("\t\t<key>phrase</key>\n")
                output.write("\t\t<string>" + pokemonCPString + "</string>\n")
                output.write("\t\t<key>shortcut</key>\n")
                # Looks at which IV type folder (i.e: Perfect or Trash)
                if ivType == "Perfect IV strings":
                    output.write("\t\t<string>p" + pokemonName + "</string>\n")
                else:
                    output.write("\t\t<string>t" + pokemonName + "</string>\n")
                output.write("\t</dict>\n")
output.write("</array>\n")
output.write("</plist>")
output.close()
