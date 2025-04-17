
def simulate_pcm_effect(section: BuildingSection, pcm_type='paraffin'):
    # Stub values - ideally connected to thermal model library
    pcm_effectiveness = {
        'paraffin': 0.25,
        'salt_hydrate': 0.3,
        'bio_pcm': 0.2
    }
    base_energy_loss = section.area * (1 / section.insulation_level) * 100
    saved_energy = base_energy_loss * pcm_effectiveness[pcm_type]
    return round(saved_energy, 2)
