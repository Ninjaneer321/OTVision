# OTVision: Python module to show home window of OTVision gui.

# Copyright (C) 2020 OpenTrafficCam Contributors
# <https://github.com/OpenTrafficCam
# <team@opentrafficcam.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import PySimpleGUI as sg
from gui import convert, detect, track, undistort, transform
from gui.helpers.sg_otc_theme import (
    OTC_ICON,
    OTC_THEME,
    OTC_FONT,
    OTC_FONTSIZE,
)

sg.SetOptions(font=(OTC_FONT, OTC_FONTSIZE))


def main():
    # Constants
    COLUMNWIDTH = 50
    ROWHEIGHT = 2
    PAD_X = 20
    PAD_Y = 20

    # # Package buttons
    ButtonConvert = sg.Button(
        "Convert h264 videos to other formats",
        size=(COLUMNWIDTH, ROWHEIGHT),
        pad=(PAD_X, PAD_Y),
        key="-BUTTONCONVERT-",
    )
    ButtonDetect = sg.Button(
        "Detect road users in videos",
        size=(COLUMNWIDTH, ROWHEIGHT),
        pad=(PAD_X, PAD_Y),
        key="-BUTTONDETECT-",
    )
    ButtonTrack = sg.Button(
        "Track road users through detections",
        size=(COLUMNWIDTH, ROWHEIGHT),
        pad=(PAD_X, PAD_Y),
        key="-BUTTONTRACK-",
    )
    ButtonUndistort = sg.Button(
        "Correct trajectories for lens distortion",
        size=(COLUMNWIDTH, ROWHEIGHT),
        pad=(PAD_X, PAD_Y),
        key="-BUTTONUNDISTORT-",
    )
    ButtonTransform = sg.Button(
        "Transform trajectories to world coordinates",
        size=(COLUMNWIDTH, ROWHEIGHT),
        pad=(PAD_X, PAD_Y),
        key="-BUTTONTRANSFORM-",
    )

    layout = [
        [ButtonConvert],
        [ButtonDetect],
        [ButtonTrack],
        [ButtonUndistort],
        [ButtonTransform],
    ]

    # # Tabs
    # TabConvert = sg.Tab(
    #     title="Convert", layout=[[sg.T("Convert")]], tooltip="Convert h264 videos"
    # )
    # TabDetect = sg.Tab(
    #     title="Detect", layout=[[sg.T("Detect")]], tooltip="Detect road users"
    # )
    # TabTrack = sg.Tab(
    #     title="Track", layout=[[sg.T("Track")]], tooltip="Track road users"
    # )
    # TabUndistort = sg.Tab(
    #     title="Undistort",
    #     layout=[[sg.T("Undistort")]],
    #     tooltip="Correct trajectories for lens distortion",
    # )
    # TabTransform = sg.Tab(
    #     title="Transform",
    #     layout=[[sg.T("Transform")]],
    #     tooltip="Transform trajectories to world coordinates",
    # )
    # TabGroup = sg.TabGroup(
    #     [[TabConvert, TabDetect, TabTrack, TabUndistort, TabTransform]]
    # )

    # Create layout
    layout = [
        [ButtonConvert],
        [ButtonDetect],
        [ButtonTrack],
        [ButtonUndistort],
        [ButtonTransform],
    ]
    # layout = [[TabGroup]]

    # Create window
    window = sg.Window(
        "OTVision: Home",
        layout,
        element_justification="center",
        icon=OTC_ICON,
        location=(0, 0),
        resizable=True,
        finalize=True,
    )
    window.maximize()

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        # Call subpackage guis by button click
        elif event == "-BUTTONCONVERT-":
            window.Hide()
            convert.main()
            window.UnHide()
            window.maximize()
        elif event == "-BUTTONDETECT-":
            window.Hide()
            detect.main()
            window.UnHide()
            window.maximize()
        elif event == "-BUTTONTRACK-":
            window.Hide()
            track.main()
            window.UnHide()
            window.maximize()
        elif event == "-BUTTONUNDISTORT-":
            window.Hide()
            undistort.main()
            window.UnHide()
            window.maximize()
        elif event == "-BUTTONTRANSFORM-":
            window.Hide()
            transform.main()
            window.UnHide()
            window.maximize()

    window.close()


if __name__ == "__main__":
    main()
