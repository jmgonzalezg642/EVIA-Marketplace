import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from 'react-native';

export default function ProfileScreen({ navigation }) {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Perfil</Text>
      </View>

      <View style={styles.profileCard}>
        <View style={styles.avatar}>
          <Text style={styles.avatarText}>👤</Text>
        </View>
        <Text style={styles.profileName}>Usuario EVIA</Text>
        <Text style={styles.profileRole}>Conductor</Text>
      </View>

      <View style={styles.menuSection}>
        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>🚗</Text>
          <Text style={styles.menuText}>Mis Compras</Text>
          <Text style={styles.menuArrow}>›</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>📋</Text>
          <Text style={styles.menuText}>Garantías</Text>
          <Text style={styles.menuArrow}>›</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.menuItem}>
          <Text style={styles.menuIcon}>⚙️</Text>
          <Text style={styles.menuText}>Configuración</Text>
          <Text style={styles.menuArrow}>›</Text>
        </TouchableOpacity>

        <TouchableOpacity 
          style={[styles.menuItem, styles.logoutButton]}
          onPress={() => navigation.replace('Login')}
        >
          <Text style={styles.menuIcon}>🚪</Text>
          <Text style={styles.logoutText}>Cerrar Sesión</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F5F9FF' },
  header: { padding: 16, paddingTop: 40, backgroundColor: '#0057B8' },
  headerTitle: { fontSize: 24, fontWeight: 'bold', color: '#FFFFFF' },
  profileCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 24,
    margin: 16,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 2,
  },
  avatar: { width: 80, height: 80, borderRadius: 40, backgroundColor: '#0057B8', justifyContent: 'center', alignItems: 'center' },
  avatarText: { fontSize: 40 },
  profileName: { fontSize: 20, fontWeight: 'bold', color: '#172033', marginTop: 12 },
  profileRole: { fontSize: 14, color: '#526075' },
  menuSection: { paddingHorizontal: 16, marginBottom: 20 },
  menuItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderRadius: 12,
    marginBottom: 8,
    shadowColor: '#000',
    shadowOpacity: 0.03,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 2,
    elevation: 1,
  },
  menuIcon: { fontSize: 20, marginRight: 12 },
  menuText: { flex: 1, fontSize: 16, color: '#172033' },
  menuArrow: { fontSize: 20, color: '#94A3B8' },
  logoutButton: { marginTop: 12 },
  logoutText: { fontSize: 16, fontWeight: '600', color: '#B91C1C' },
});