import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, TextInput } from 'react-native';
import { getProducts } from '../services/eviaService';

export default function CatalogScreen() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');

  useEffect(() => {
    loadProducts();
  }, []);

  async function loadProducts() {
    try {
      setLoading(true);
      const data = await getProducts();
      setProducts(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  const filteredProducts = products.filter(p =>
    p.marca.toLowerCase().includes(search.toLowerCase()) ||
    p.modelo.toLowerCase().includes(search.toLowerCase())
  );

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <View style={styles.cardContent}>
        <View>
          <Text style={styles.cardTitle}>{item.marca} {item.modelo}</Text>
          <Text style={styles.cardSubtitle}>⚡ {item.autonomia_km} km • {item.tipo_vehiculo}</Text>
          <Text style={styles.cardStatus}>
            {item.es_nuevo ? '🆕 Nuevo' : '🔄 Usado'}
          </Text>
        </View>
        <View style={styles.cardRight}>
          <Text style={styles.cardPrice}>${Number(item.precio).toLocaleString()}</Text>
          <TouchableOpacity style={styles.viewButton}>
            <Text style={styles.viewButtonText}>Ver</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Explore EVs</Text>
        <View style={styles.searchContainer}>
          <TextInput
            style={styles.searchInput}
            placeholder="Search EVs..."
            value={search}
            onChangeText={setSearch}
          />
        </View>
      </View>

      <FlatList
        data={filteredProducts}
        renderItem={renderItem}
        keyExtractor={(item) => String(item.id)}
        contentContainerStyle={styles.list}
        showsVerticalScrollIndicator={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F5F9FF' },
  header: { padding: 16, paddingTop: 40, backgroundColor: '#0057B8' },
  headerTitle: { fontSize: 24, fontWeight: 'bold', color: '#FFFFFF', marginBottom: 12 },
  searchContainer: { backgroundColor: '#FFFFFF', borderRadius: 10, paddingHorizontal: 12 },
  searchInput: { fontSize: 16, paddingVertical: 10 },
  list: { padding: 16 },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 2,
  },
  cardContent: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  cardTitle: { fontSize: 16, fontWeight: 'bold', color: '#172033' },
  cardSubtitle: { fontSize: 13, color: '#526075', marginTop: 2 },
  cardStatus: { fontSize: 12, fontWeight: '600', color: '#166534', marginTop: 4 },
  cardRight: { alignItems: 'flex-end' },
  cardPrice: { fontSize: 16, fontWeight: 'bold', color: '#0057B8' },
  viewButton: { backgroundColor: '#0057B8', borderRadius: 8, paddingHorizontal: 16, paddingVertical: 6, marginTop: 6 },
  viewButtonText: { color: '#FFFFFF', fontSize: 12, fontWeight: '600' },
});