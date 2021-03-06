from tgthemegen.generate import Color, ColorSource, ColorProperty

import colorsys
import binascii
import pprint

# Breeze v3 by @vmorenomarin
breeze_v3 = {
    'windowBg': '#eff0f1',
    'windowFg': '#000000',
    'windowBgOver': '#f1f1f1',
    'windowBgRipple': '#e5e5e5',
    'windowFgOver': 'windowFg',
    'windowSubTextFg': '#7f8c8d',
    'windowSubTextFgOver': '#31363b',
    'windowBoldFg': '#222222',
    'windowBoldFgOver': '#222222',
    'windowBgActive': '#3daee9',
    'windowFgActive': '#ffffff',
    'windowActiveTextFg': '#168acd',
    'windowShadowFg': '#000000',
    'windowShadowFgFallback': '#f1f1f1',
    'shadowFg': '#00000018',
    'slideFadeOutBg': '#0000003c',
    'slideFadeOutShadowFg': 'windowShadowFg',
    'imageBg': '#000000',
    'imageBgTransparent': '#ffffff',
    'activeButtonBg': 'windowBgActive',
    'activeButtonBgOver': '#39a5db',
    'activeButtonBgRipple': '#2095d0',
    'activeButtonFg': 'windowFgActive',
    'activeButtonFgOver': 'activeButtonFg',
    'activeButtonSecondaryFg': '#cceeff',
    'activeButtonSecondaryFgOver': 'activeButtonSecondaryFg',
    'activeLineFg': '#37a1de',
    'activeLineFgError': '#e48383',
    'lightButtonBg': 'windowBg',
    'lightButtonBgOver': '#93cee9',
    'lightButtonBgRipple': '#c9e4f6',
    'lightButtonFg': 'windowActiveTextFg',
    'lightButtonFgOver': 'lightButtonFg',
    'attentionButtonFg': '#d14e4e',
    'attentionButtonFgOver': '#d14e4e',
    'attentionButtonBgOver': '#fcdfde',
    'attentionButtonBgRipple': '#f4c3c2',
    'outlineButtonBg': 'windowBg',
    'outlineButtonBgOver': 'lightButtonBgOver',
    'outlineButtonOutlineFg': 'windowBgActive',
    'outlineButtonBgRipple': 'lightButtonBgRipple',
    'menuBg': 'windowBg',
    'menuBgOver': 'windowBgOver',
    'menuBgRipple': 'windowBgRipple',
    'menuIconFg': '#31363b',
    'menuIconFgOver': '#93cee9',
    'menuSubmenuArrowFg': '#373737',
    'menuFgDisabled': '#cccccc',
    'menuSeparatorFg': '#f1f1f1',
    'scrollBarBg': '#3daee9',
    'scrollBarBgOver': '#93cee9',
    'scrollBg': '#bfc0c2',
    'scrollBgOver': '#bfc0c2',
    'smallCloseIconFg': '#c7c7c7',
    'smallCloseIconFgOver': '#a3a3a3',
    'radialFg': 'windowFgActive',
    'radialBg': '#00000056',
    'placeholderFg': 'windowSubTextFg',
    'placeholderFgActive': '#aaaaaa',
    'inputBorderFg': '#e0e0e0',
    'filterInputBorderFg': '#54c3f3',
    'checkboxFg': '#b3b3b3',
    'sliderBgInactive': '#e1eaef',
    'sliderBgActive': 'windowBgActive',
    'tooltipBg': '#eef2f5',
    'tooltipFg': '#5d6c80',
    'tooltipBorderFg': '#c9d1db',
    'titleBg': 'windowBgOver',
    'titleShadow': '#00000003',
    'titleButtonFg': '#ababab',
    'titleButtonBgOver': '#e5e5e5',
    'titleButtonFgOver': '#9a9a9a',
    'titleButtonCloseBgOver': '#e81123',
    'titleButtonCloseFgOver': 'windowFgActive',
    'titleFgActive': '#3e3c3e',
    'titleFg': '#acacac',
    'trayCounterBg': '#f23c34',
    'trayCounterBgMute': '#888888',
    'trayCounterFg': '#ffffff',
    'trayCounterBgMacInvert': '#ffffff',
    'trayCounterFgMacInvert': '#ffffff01',
    'layerBg': '#0000007f',
    'cancelIconFg': 'menuIconFg',
    'cancelIconFgOver': 'menuIconFgOver',
    'boxBg': 'windowBg',
    'boxTextFg': 'windowFg',
    'boxTextFgGood': '#4ab44a',
    'boxTextFgError': '#d84d4d',
    'boxTitleFg': '#404040',
    'boxSearchBg': 'boxBg',
    'boxSearchCancelIconFg': 'cancelIconFg',
    'boxSearchCancelIconFgOver': 'cancelIconFgOver',
    'boxTitleAdditionalFg': '#808080',
    'boxTitleCloseFg': 'cancelIconFg',
    'boxTitleCloseFgOver': 'cancelIconFgOver',
    'membersAboutLimitFg': 'windowSubTextFgOver',
    'contactsBg': 'windowBg',
    'contactsBgOver': '#93cee9',
    'contactsNameFg': 'boxTextFg',
    'contactsStatusFg': 'windowSubTextFg',
    'contactsStatusFgOver': 'windowSubTextFgOver',
    'contactsStatusFgOnline': 'windowActiveTextFg',
    'photoCropFadeBg': 'layerBg',
    'photoCropPointFg': '#ffffff7f',
    'introBg': 'windowBg',
    'introTitleFg': 'windowBoldFg',
    'introDescriptionFg': 'windowSubTextFg',
    'introErrorFg': 'windowSubTextFg',
    'introCoverTopBg': '#0f89d0',
    'introCoverBottomBg': '#39b0f0',
    'introCoverIconsFg': '#5ec6ff',
    'introCoverPlaneTrace': '#5ec6ff69',
    'introCoverPlaneInner': '#c6d8e8',
    'introCoverPlaneOuter': '#a1bed4',
    'introCoverPlaneTop': '#ffffff',
    'dialogsMenuIconFg': 'menuIconFg',
    'dialogsMenuIconFgOver': 'menuIconFgOver',
    'dialogsBg': 'windowBg',
    'dialogsNameFg': 'windowBoldFg',
    'dialogsChatIconFg': 'dialogsNameFg',
    'dialogsDateFg': 'windowSubTextFg',
    'dialogsTextFg': 'windowSubTextFg',
    'dialogsTextFgService': 'windowActiveTextFg',
    'dialogsDraftFg': '#dd4b39',
    'dialogsVerifiedIconBg': 'windowBgActive',
    'dialogsVerifiedIconFg': 'windowFgActive',
    'dialogsSendingIconFg': '#c1c1c1',
    'dialogsSentIconFg': '#3daee9',
    'dialogsUnreadBg': 'windowBgActive',
    'dialogsUnreadBgMuted': '#31363b',
    'dialogsUnreadFg': 'windowFgActive',
    'dialogsBgOver': 'windowBgOver',
    'dialogsNameFgOver': 'windowBoldFgOver',
    'dialogsChatIconFgOver': 'dialogsNameFgOver',
    'dialogsDateFgOver': 'windowSubTextFgOver',
    'dialogsTextFgOver': 'windowSubTextFgOver',
    'dialogsTextFgServiceOver': 'dialogsTextFgService',
    'dialogsDraftFgOver': 'dialogsDraftFg',
    'dialogsVerifiedIconBgOver': 'dialogsVerifiedIconBg',
    'dialogsVerifiedIconFgOver': 'dialogsVerifiedIconFg',
    'dialogsSendingIconFgOver': 'dialogsSendingIconFg',
    'dialogsSentIconFgOver': 'dialogsSentIconFg',
    'dialogsUnreadBgOver': 'dialogsUnreadBg',
    'dialogsUnreadBgMutedOver': 'dialogsUnreadBgMuted',
    'dialogsUnreadFgOver': 'dialogsUnreadFg',
    'dialogsBgActive': '#3aacea',
    'dialogsNameFgActive': 'windowFgActive',
    'dialogsChatIconFgActive': 'dialogsNameFgActive',
    'dialogsDateFgActive': 'windowFgActive',
    'dialogsTextFgActive': 'windowFgActive',
    'dialogsTextFgServiceActive': 'dialogsTextFgActive',
    'dialogsDraftFgActive': '#c6e1f7',
    'dialogsVerifiedIconBgActive': 'dialogsTextFgActive',
    'dialogsVerifiedIconFgActive': 'dialogsBgActive',
    'dialogsSendingIconFgActive': '#ffffff99',
    'dialogsSentIconFgActive': 'dialogsTextFgActive',
    'dialogsUnreadBgActive': 'dialogsTextFgActive',
    'dialogsUnreadBgMutedActive': 'dialogsDraftFgActive',
    'dialogsUnreadFgActive': 'dialogsBgActive',
    'dialogsForwardBg': 'dialogsBgActive',
    'dialogsForwardFg': 'dialogsNameFgActive',
    'searchedBarBg': 'windowBgOver',
    'searchedBarBorder': 'shadowFg',
    'searchedBarFg': 'windowSubTextFgOver',
    'topBarBg': 'windowBg',
    'emojiPanBg': 'windowBg',
    'emojiPanCategories': 'windowBg',
    'emojiPanHeaderFg': 'windowSubTextFg',
    'emojiPanHeaderBg': 'emojiPanBg',
    'stickerPanDeleteBg': '#000000cc',
    'stickerPanDeleteFg': 'windowFgActive',
    'stickerPreviewBg': '#ffffffb0',
    'historyTextInFg': 'windowFg',
    'historyTextOutFg': 'windowFg',
    'historyCaptionInFg': 'historyTextInFg',
    'historyCaptionOutFg': 'historyTextOutFg',
    'historyFileNameInFg': 'historyTextInFg',
    'historyFileNameOutFg': 'historyTextOutFg',
    'historyOutIconFg': 'dialogsSentIconFg',
    'historyOutIconFgSelected': '#4da79f',
    'historyIconFgInverted': 'windowFgActive',
    'historySendingOutIconFg': '#98d292',
    'historySendingInIconFg': '#a0adb5',
    'historySendingInvertedIconFg': '#ffffffc8',
    'historySystemBg': '#89a0b47f',
    'historySystemBgSelected': '#bbc8d4a2',
    'historySystemFg': 'windowFgActive',
    'historyUnreadBarBg': '#fcfbfa',
    'historyUnreadBarBorder': 'shadowFg',
    'historyUnreadBarFg': '#538bb4',
    'historyForwardChooseBg': '#0000004c',
    'historyForwardChooseFg': 'windowFgActive',
    'historyPeer1NameFg': '#c03d33',
    'historyPeer1UserpicBg': '#e17076',
    'historyPeer2NameFg': '#4fad2d',
    'historyPeer2UserpicBg': '#7bc862',
    'historyPeer3NameFg': '#d09306',
    'historyPeer3UserpicBg': '#e5ca77',
    'historyPeer4NameFg': 'windowActiveTextFg',
    'historyPeer4UserpicBg': '#65aadd',
    'historyPeer5NameFg': '#8544d6',
    'historyPeer5UserpicBg': '#a695e7',
    'historyPeer6NameFg': '#cd4073',
    'historyPeer6UserpicBg': '#ee7aae',
    'historyPeer7NameFg': '#2996ad',
    'historyPeer7UserpicBg': '#6ec9cb',
    'historyPeer8NameFg': '#ce671b',
    'historyPeer8UserpicBg': '#faa774',
    'historyPeerUserpicFg': 'windowFgActive',
    'historyScrollBarBg': '#3daee9',
    'historyScrollBarBgOver': '#93cee9',
    'historyScrollBg': '#bfc0c2',
    'historyScrollBgOver': '#bfc0c2',
    'msgInBg': 'windowBg',
    'msgInBgSelected': '#c2dcf2',
    'msgOutBg': '#F0FDFF',
    'msgOutBgSelected': '#b7dbdb',
    'msgSelectOverlay': '#358cd44c',
    'msgStickerOverlay': '#358cd47f',
    'msgInServiceFg': 'windowActiveTextFg',
    'msgInServiceFgSelected': 'windowActiveTextFg',
    'msgOutServiceFg': '#3a8e26',
    'msgOutServiceFgSelected': '#367570',
    'msgInShadow': '#748ea229',
    'msgInShadowSelected': '#548dbb29',
    'msgOutShadow': '#3ac34740',
    'msgOutShadowSelected': '#37a78e40',
    'msgInDateFg': '#a0acb6',
    'msgInDateFgSelected': '#6a9cc5',
    'msgOutDateFg': '#807e7d',
    'msgOutDateFgSelected': '#50a79c',
    'msgServiceFg': 'windowFgActive',
    'msgServiceBg': '#556e837f',
    'msgServiceBgSelected': '#8ca0b3a2',
    'msgInReplyBarColor': 'activeLineFg',
    'msgInReplyBarSelColor': 'activeLineFg',
    'msgOutReplyBarColor': 'historyOutIconFg',
    'msgOutReplyBarSelColor': 'historyOutIconFgSelected',
    'msgImgReplyBarColor': 'msgServiceFg',
    'msgInMonoFg': '#4e7391',
    'msgOutMonoFg': '#469165',
    'msgDateImgFg': 'msgServiceFg',
    'msgDateImgBg': '#00000054',
    'msgDateImgBgOver': '#00000074',
    'msgDateImgBgSelected': '#1c4a7187',
    'msgFileThumbLinkInFg': 'lightButtonFg',
    'msgFileThumbLinkInFgSelected': 'lightButtonFgOver',
    'msgFileThumbLinkOutFg': '#5eba5b',
    'msgFileThumbLinkOutFgSelected': '#31a298',
    'msgFileInBg': 'windowBgActive',
    'msgFileInBgOver': '#4eade3',
    'msgFileInBgSelected': '#51a3d3',
    'msgFileOutBg': '#3daee9',
    'msgFileOutBgOver': '#6bc272',
    'msgFileOutBgSelected': '#5fb389',
    'msgFile1Bg': '#72b1df',
    'msgFile1BgDark': '#5c9ece',
    'msgFile1BgOver': '#5294c4',
    'msgFile1BgSelected': '#5099d0',
    'msgFile2Bg': '#61b96e',
    'msgFile2BgDark': '#4da859',
    'msgFile2BgOver': '#44a050',
    'msgFile2BgSelected': '#46a07e',
    'msgFile3Bg': '#e47272',
    'msgFile3BgDark': '#cd5b5e',
    'msgFile3BgOver': '#c35154',
    'msgFile3BgSelected': '#9f6a82',
    'msgFile4Bg': '#efc274',
    'msgFile4BgDark': '#e6a561',
    'msgFile4BgOver': '#dc9c5a',
    'msgFile4BgSelected': '#b19d84',
    'msgWaveformInActive': 'windowBgActive',
    'msgWaveformInActiveSelected': '#51a3d3',
    'msgWaveformInInactive': '#807e7d',
    'msgWaveformInInactiveSelected': '#9cc1e1',
    'msgWaveformOutActive': '#31363b',
    'msgWaveformOutActiveSelected': '#6badad',
    'msgWaveformOutInactive': '#807e7d',
    'msgWaveformOutInactiveSelected': '#91c3c3',
    'msgBotKbOverBgAdd': '#ffffff20',
    'msgBotKbIconFg': 'msgServiceFg',
    'msgBotKbRippleBg': '#00000020',
    'mediaInFg': 'msgInDateFg',
    'mediaInFgSelected': 'msgInDateFgSelected',
    'mediaOutFg': 'msgOutDateFg',
    'mediaOutFgSelected': 'msgOutDateFgSelected',
    'youtubePlayIconBg': '#e83131c8',
    'youtubePlayIconFg': 'windowFgActive',
    'videoPlayIconBg': '#0000007f',
    'videoPlayIconFg': '#ffffff',
    'toastBg': '#000000b2',
    'toastFg': 'windowFgActive',
    'reportSpamBg': 'emojiPanHeaderBg',
    'reportSpamFg': 'windowFg',
    'historyToDownShadow': '#00000040',
    'historyComposeAreaBg': 'msgInBg',
    'historyComposeAreaFg': 'historyTextInFg',
    'historyComposeAreaFgService': 'msgInDateFg',
    'historyComposeIconFg': 'menuIconFg',
    'historyComposeIconFgOver': 'menuIconFgOver',
    'historySendIconFg': 'windowBgActive',
    'historySendIconFgOver': 'windowBgActive',
    'historyPinnedBg': 'historyComposeAreaBg',
    'historyReplyBg': 'historyComposeAreaBg',
    'historyReplyCancelFg': 'cancelIconFg',
    'historyReplyCancelFgOver': 'cancelIconFgOver',
    'historyComposeButtonBg': 'historyComposeAreaBg',
    'historyComposeButtonBgOver': '#93cee9',
    'historyComposeButtonBgRipple': 'windowBgRipple',
    'overviewCheckBg': '#00000040',
    'overviewCheckFg': 'windowBg',
    'overviewCheckFgActive': 'windowBg',
    'overviewPhotoSelectOverlay': '#40ace333',
    'profileStatusFgOver': '#7c99b2',
    'notificationsBoxMonitorFg': '#eff0f1B2',
    'notificationsBoxScreenBg': 'dialogsBgActive',
    'notificationSampleUserpicFg': 'windowBgActive',
    'notificationSampleCloseFg': 'windowSubTextFg',
    'notificationSampleTextFg': 'windowSubTextFg',
    'notificationSampleNameFg': 'windowSubTextFg',
    'mainMenuBg': 'windowBg',
    'mainMenuCoverBg': 'dialogsBgActive',
    'mainMenuCoverFg': 'windowFgActive',
    'mediaPlayerBg': 'windowBg',
    'mediaPlayerActiveFg': 'windowBgActive',
    'mediaPlayerInactiveFg': 'sliderBgInactive',
    'mediaPlayerDisabledFg': '#9dd1ef',
    'mediaviewFileBg': 'windowBg',
    'mediaviewFileNameFg': 'windowFg',
    'mediaviewFileSizeFg': 'windowSubTextFg',
    'mediaviewFileRedCornerFg': '#d55959',
    'mediaviewFileYellowCornerFg': '#e8a659',
    'mediaviewFileGreenCornerFg': '#49a957',
    'mediaviewFileBlueCornerFg': '#599dcf',
    'mediaviewFileExtFg': 'activeButtonFg',
    'mediaviewMenuBg': '#383838',
    'mediaviewMenuBgOver': '#505050',
    'mediaviewMenuBgRipple': '#676767',
    'mediaviewMenuFg': 'windowFgActive',
    'mediaviewBg': '#222222eb',
    'mediaviewVideoBg': 'imageBg',
    'mediaviewControlBg': '#0000003c',
    'mediaviewControlFg': 'windowFgActive',
    'mediaviewCaptionBg': '#11111180',
    'mediaviewCaptionFg': 'mediaviewControlFg',
    'mediaviewTextLinkFg': '#91d9ff',
    'mediaviewSaveMsgBg': 'toastBg',
    'mediaviewSaveMsgFg': 'toastFg',
    'mediaviewPlaybackActive': '#c7c7c7',
    'mediaviewPlaybackInactive': '#252525',
    'mediaviewPlaybackActiveOver': '#ffffff',
    'mediaviewPlaybackInactiveOver': '#474747',
    'mediaviewPlaybackProgressFg': '#ffffffc7',
    'mediaviewPlaybackIconFg': 'mediaviewPlaybackActive',
    'mediaviewPlaybackIconFgOver': 'mediaviewPlaybackActiveOver',
    'mediaviewTransparentBg': '#ffffff',
    'mediaviewTransparentFg': '#cccccc',
    'notificationBg': 'windowBg'}


def detect_property(value: Color, accent: Color, primary: Color, foreground: Color, background: Color):
    value_hsv = colorsys.rgb_to_hsv(*value.channels[:3])
    accent_hsv = colorsys.rgb_to_hsv(*accent.channels[:3])
    primary_hsv = colorsys.rgb_to_hsv(*primary.channels[:3])
    foreground_hsv = colorsys.rgb_to_hsv(*foreground.channels[:3])
    background_hsv = colorsys.rgb_to_hsv(*background.channels[:3])
    near_options = [
        (accent_hsv, accent, 'accent'),
        (primary_hsv, primary, 'primary'),
        (foreground_hsv, foreground, 'foreground'),
        (background_hsv, background, 'background')]

    def similarity(sample_a, sample_b):
        return 3.0 - (
            abs(sample_a[0] - sample_b[0]) +
            abs(sample_a[1] - sample_b[1]) +
            abs(sample_a[2] - sample_b[2]))
    near_options.sort(key=lambda x: similarity(x[1].channels, value_hsv))
    nearest_source = near_options[0]
    return [
        nearest_source[2],
        [(a / b if b > 0.0 else 1.0) for a, b in zip(value.channels, nearest_source[0])]]


def detect_properties(sample, accent: Color, primary: Color, foreground: Color, background: Color):
    props = {}
    for k, v in sample.items():
        if v[0] == '#':
            color = Color.from_channels([b / 255 for b in binascii.unhexlify(v.encode()[1:])])
            props[k] = detect_property(color, accent, primary, foreground, background)
        else:
            props[k] = v
    return props


if __name__ == '__main__':
    pprint.pprint(detect_properties(
        sample=breeze_v3,
        accent=Color.parse('#3daee9'),
        primary=Color.parse('#3daee9'),
        foreground=Color.parse('#000000'),
        background=Color.parse('#eff0f1')))
