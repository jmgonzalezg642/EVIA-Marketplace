import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, StyleSheet, ActivityIndicator } from 'react-native';
import { getProducts } from './src/services/eviaService';

export default function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadProducts() {
      try {
        setLoading(true);
        const data = await getProducts();
        setProducts(data);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    loadProducts();
  }, []);

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#0057B8" />
        <Text style={styles.loadingText}>Cargando vehículos...</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.center}>
        <Text style={styles.errorText}>Error: {error}</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>🚗 EVIA</Text>
        <Text style={styles.subtitle}>Conduciendo hacia el futuro</Text>
      </View>
      <FlatList
        data={products}
        keyExtractor={(item) => String(item.id)}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>{item.marca} {item.modelo}</Text>
            <Text style={styles.cardPrice}>💰 ${Number(item.precio).toLocaleString()}</Text>
            <Text style={styles.cardDetail}>📦 {item.tipo_vehiculo}</Text>
            <Text style={styles.cardDetail}>⚡ {item.autonomia_km} km</Text>
            <Text style={styles.cardStatus}>
              {item.es_nuevo ? '🆕 Nuevo' : '🔄 Usado'}
            </Text>
          </View>
        )}
        contentContainerStyle={styles.list}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f5f5f5' },
  header: {
    backgroundColor: '#0057B8',
    padding: 20,
    paddingTop: 50,
    paddingBottom: 15,
    alignItems: 'center',
  },
  title: { fontSize: 28, fontWeight: 'bold', color: '#fff' },
  subtitle: { fontSize: 14, color: '#fff', marginTop: 4 },
  center: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  list: { padding: 16 },
  card: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  cardTitle: { fontSize: 18, fontWeight: 'bold', color: '#172033' },
  cardPrice: { fontSize: 16, fontWeight: '600', color: '#0057B8', marginTop: 4 },
  cardDetail: { fontSize: 14, color: '#526075', marginTop: 2 },
  cardStatus: { fontSize: 14, fontWeight: 'bold', color: '#166534', marginTop: 6 },
  loadingText: { marginTop: 12, fontSize: 16, color: '#526075' },
  errorText: { fontSize: 16, color: '#B91C1C', textAlign: 'center' },
});
