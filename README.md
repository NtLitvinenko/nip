# NIP - New Internet Protocol
NIP Using IPv4, but has IPv6 support!<br>
I specially made a new browser <a href="https://github.com/NTLitvinenko/Jelly" target="_blank">(Jelly!)</a><br>
I have created a new "markup file" for it!<br>
NMF - NIP Markup File like: <br>
```
# NIP Markup File (nipmf = nmf)
# markuptype_Varname:style
# style_Stylename:styles like
# style_Button1:{bgcolor=red;text=Click me!;x=10;y=10}
# remove spaces if needed
style_Button1:{bgcolor=red;text=Click me!;x=10;y=10}
style_Label1:{text=Hi, world!;x=50;y=50}
style_btn:{text=Button clicked!!!;background=black;foreground=white;x=255;y=255}
label_Hello:style_Label1
button_Button:style_Button1
button_Button.onclick:function_OnButtonClick
function_OnButtonClick{
    label_Label1=style_NewStyle
    exec:print?Hello World[?]
    exec:destroy?label_Hello
    exec:createWidget?label_Hi?style_btn
}
```
