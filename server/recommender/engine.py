
def generate_recommendations(changes):
    recommendations = []
    for change in changes:
        if change["change"] == "removed":
            recommendations.append({
                "action": "revisar",
                "file": change["file"],
                "sugerencia": "Este archivo ha sido eliminado, verifique si hay reemplazos."
            })
        elif change["change"] == "modified":
            recommendations.append({
                "action": "analizar",
                "file": change["file"],
                "sugerencia": "Archivo modificado, inspeccionar funciones clave."
            })
        elif change["change"] == "added":
            recommendations.append({
                "action": "nuevo",
                "file": change["file"],
                "sugerencia": "Nuevo archivo detectado."
            })
    return recommendations
