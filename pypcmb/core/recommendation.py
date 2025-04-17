
def recommend_pcm_placement(profile: BuildingProfile):
    recommendations = []
    for section in profile.sections:
        score = (
            section.exposure_to_sunlight * 0.5 +
            (1 / section.insulation_level) * 0.3 +
            (section.area / 100.0) * 0.2
        )
        
        if score > 0.5:
            recommendations.append({
                'section': section.type,
                'orientation': section.orientation,
                'recommendation': 'Integrate PCM',
                'score': round(score, 2)
            })
    return recommendations
