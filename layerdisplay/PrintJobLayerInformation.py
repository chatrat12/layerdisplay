class PrintJobLayerInformation:
	def __init__(self, layerChangePositions):
		self._layer_change_positions = layerChangePositions

	def get_layer_count(self):
		return len(self._layer_change_positions)

	def get_layer_change_position(self, layer_index):
		if layer_index >= len(self._layer_change_positions):
			return 1
		return self._layer_change_positions[layer_index]
