import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "Codechef Scrapper"

    Item{
        id: page
        visible: true

        width: parent.width

        Rectangle{
            height: {
             console.log("comment ")
             return 160
            }
            width: parent.width
            color: "#ff0000"

            Text{
                id: mainText
                text: " Enter Handle "
                height: 50
                width: parent.width
                font.pixelSize: 12
                font.italic: true
                horizontalAlignment: Text.AlignHCenter

            }

            Button{
            id: mainButton
            text: "up"
            anchors.top: mainText.bottom
                onClicked: {
                    if(mainButton.text="up"){
                        mainButton.text="down"
                     }else {
                        mainButton.text="up"
                     }

                }
            }
        }
    }
}