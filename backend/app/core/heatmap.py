def generate_heatmap_data(events):
    """Generate heatmap coordinates from click/hover events."""
    heatmap = {}
    for event in events:
        if event.coordinates:
            coords = event.coordinates.split(',')
            key = f"{coords[0]}_{coords[1]}"
            heatmap[key] = heatmap.get(key, 0) + 1
    return heatmap
