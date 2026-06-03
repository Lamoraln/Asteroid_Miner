#include "include/LinkedList.h"
#include "include/BST.h"

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    // -------------------------
    // LEER JSON
    // -------------------------

    std::ifstream file(
        "data/game_state.json"
    );

    if(!file.is_open())
    {
        std::cout
            << "Cannot open game_state.json"
            << std::endl;

        return 1;
    }

    std::stringstream buffer;

    buffer << file.rdbuf();

    std::string json =
        buffer.str();

    file.close();

    // -------------------------
    // ELIMINAR ESPACIOS
    // -------------------------

    std::string compact;

    for(char c : json)
    {
        if(
            c != ' ' &&
            c != '\n' &&
            c != '\t' &&
            c != '\r'
        )
        {
            compact += c;
        }
    }

    json = compact;

    // -------------------------
    // EXTRAER LEVEL
    // -------------------------

    int level = 0;
    int resources = 0;
    int stars = 0;

    size_t levelPos =
        json.find("\"level\":");

    if(levelPos != std::string::npos)
    {
        levelPos += 8;

        size_t end =
            json.find(
                ",",
                levelPos
            );

        level =
            std::stoi(
                json.substr(
                    levelPos,
                    end - levelPos
                )
            );
    }

    // -------------------------
    // EXTRAER RESOURCES
    // -------------------------

    size_t resourcesPos =
        json.find("\"resources\":");

    if(resourcesPos != std::string::npos)
    {
        resourcesPos += 12;

        size_t end =
            json.find(
                ",",
                resourcesPos
            );

        resources =
            std::stoi(
                json.substr(
                    resourcesPos,
                    end - resourcesPos
                )
            );
    }

    // -------------------------
    // EXTRAER STARS
    // -------------------------

    size_t starsPos =
        json.find("\"stars\":");

    if(starsPos != std::string::npos)
    {
        starsPos += 8;

        size_t end =
            json.find(
                ",",
                starsPos
            );

        stars =
            std::stoi(
                json.substr(
                    starsPos,
                    end - starsPos
                )
            );
    }

    // -------------------------
    // ESTRUCTURAS
    // -------------------------

    LinkedList history;

    BST catalog;

    std::string route_string;

    // -------------------------
    // CREAR BST
    // -------------------------

    size_t catalogPos = 0;

    while(
        (
            catalogPos =
            json.find(
                "\"name\":\"",
                catalogPos
            )
        )
        != std::string::npos
    )
    {
        catalogPos += 8;

        size_t end =
            json.find(
                "\"",
                catalogPos
            );

        std::string asteroidName =
            json.substr(
                catalogPos,
                end - catalogPos
            );

        size_t valuePos =
            json.find(
                "\"value\":",
                end
            );

        valuePos += 8;

        size_t valueEnd =
            json.find_first_of(
                ",}",
                valuePos
            );

        int asteroidValue =
            std::stoi(
                json.substr(
                    valuePos,
                    valueEnd - valuePos
                )
            );

        catalog.insert(
            asteroidName,
            asteroidValue
        );

        catalogPos = end;
    }

    // -------------------------
    // CREAR RUTA
    // -------------------------

    size_t pos = 0;

    while(
        (
            pos =
            json.find(
                "\"name\":\"",
                pos
            )
        )
        != std::string::npos
    )
    {
        pos += 8;

        size_t end =
            json.find(
                "\"",
                pos
            );

        std::string asteroid =
            json.substr(
                pos,
                end - pos
            );

        if(!route_string.empty())
        {
            route_string += "->";
        }

        route_string += asteroid;

        pos = end;
    }

    std::string history_entry =
        "Level " +
        std::to_string(level) +
        " | Resources " +
        std::to_string(resources) +
        " | Stars " +
        std::to_string(stars) +
        " | " +
        route_string;

    history.insert(
        history_entry
    );

    history.appendToFile(
        "data/route_history.txt"
    );

    // -------------------------
    // MOSTRAR RESUMEN
    // -------------------------

    std::cout
        << "\nGAME SUMMARY\n"
        << std::endl;

    std::cout
        << "Level: "
        << level
        << std::endl;

    std::cout
        << "Resources: "
        << resources
        << std::endl;

    std::cout
        << "Stars: "
        << stars
        << std::endl;

    // -------------------------
    // MOSTRAR HISTORIAL
    // -------------------------

    std::cout
        << "\nROUTE HISTORY\n"
        << std::endl;

    history.print();

    // -------------------------
    // MOSTRAR BST
    // -------------------------

    std::cout
        << "\nASTEROID CATALOG\n"
        << std::endl;

    catalog.inorder();

    // -------------------------
    // OUTPUT.JSON
    // -------------------------

    std::ofstream output(
        "data/output.json"
    );

    output
        << "{\n"
        << "\"status\":\"ok\",\n"
        << "\"level\":"
        << level
        << ",\n"
        << "\"resources\":"
        << resources
        << ",\n"
        << "\"stars\":"
        << stars
        << ",\n"
        << "\"route_saved\":\""
        << route_string
        << "\"\n"
        << "}";

    output.close();

    return 0;
}