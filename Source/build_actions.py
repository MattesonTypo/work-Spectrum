"""Custom actions for the msfl build system. Referenced from build.yaml."""

import re
from msfontlib.build.actions import post_action, pre_action


@post_action("load_glyphs_source")
def filter_bg_layers(context, argument):
    for glyph in context.gs_font.glyphs:
        for layer in glyph.layers:
            if layer.hasBackground:
                # HACK: since there is no method to delete background layers.
                layer._background = None

@post_action("post_processing")
def remove_name_id(context, argument):
    nid_to_remove = [int(nid) for nid in re.findall(r'\d+', argument)]
    name_table = context.tt_font["name"]
    for n in name_table.names:
        if n.nameID in nid_to_remove:
            name_table.removeNames(n.nameID, n.platformID, n.platEncID, n.langID)

@post_action("post_processing")
def remove_tables(context, argument):
    tables_to_remove = argument.split(",")
    for table in tables_to_remove:
        if table in context.tt_font:
            del context.tt_font[table]