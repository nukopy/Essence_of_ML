#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import Figure, output_file, show

output_file("slider.html")

t = [t*0.001 for t in range(0, 1000)]
v = t

source = ColumnDataSource(data=dict(t=t, v=v))

plot = Figure(plot_width=400, plot_height=200, x_range=[0, 1], y_range=[-100, 100])
plot.line(x='t', y='v', source=source, line_width=3, line_alpha=0.6)

freq = Slider(start=1, end=100, value=50, step=1, title="freqency")
amp = Slider(start=1, end=100, value=50, step=1, title="amplitude")

callback = CustomJS(args=dict(source=source, freq=freq, amp=amp), code="""
    var data = source.data;
    var f = freq.value
    var a = amp.value
    t = data['t']
    v = data['v']
    for (i = 0; i < t.length; i++) {
    v[i] = a*Math.sin(f*t[i])
    }
    source.change.emit();
    """)

layout = column(plot, freq, amp)
freq.js_on_change('value', callback)
amp.js_on_change('value', callback)

show(layout)
