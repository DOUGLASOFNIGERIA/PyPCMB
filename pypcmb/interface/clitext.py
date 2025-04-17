def display_results(recommendations, profile):
    print(f"Recommendations for climate zone: {profile.climate_zone}")
    for rec in recommendations:
        print(
            f"- Place PCM in {rec['section']} (Orientation: {rec['orientation']}), "
            f"Score: {rec['score']}"
        )
