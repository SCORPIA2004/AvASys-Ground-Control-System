import QtQuick 2.9
import QtQuick.Window 2.2
import QtQuick.Controls 2.2

Item{
    Rectangle{
        id:rect1
        color:"yellow"
        anchors.fill: parent
        Text {
            id: sampleText1
            text: qsTr("This text should appear")
            font.family: "Arial"
            font.pointSize: 50
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.fill: parent
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }
    }

}
/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/