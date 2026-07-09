import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Alert,
  ActivityIndicator,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { loginUser } from '../services/eviaService';

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState('prueba@evia.com');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    if (!email.trim()) {
      Alert.alert('Error', 'Por favor ingresa tu correo electrónico');
      return;
    }

    setLoading(true);
    try {
      const result = await loginUser(email);
      Alert.alert('Éxito', `Bienvenido ${result.user.name}`);
      navigation.replace('HomeTabs');
    } catch (error) {
      Alert.alert('Error', error.message || 'Credenciales inválidas');
    } finally {
      setLoading(false);
    }
  };

  const usuariosDemo = [
    { email: 'prueba@evia.com', name: 'Usuario de prueba' },
    { email: 'carlos@evia.com', name: 'Carlos Vendedor' },
    { email: 'ventas@tesla.com', name: 'Tesla Colombia' },
    { email: 'daniela@hotmail.com', name: 'Daniela Gil' },
    { email: 'luis@hotmail.com', name: 'Luis Sanabria' },
  ];

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <View style={styles.content}>
        <Text style={styles.logo}>⚡</Text>
        <Text style={styles.title}>EVIA</Text>
        <Text style={styles.subtitle}>Iniciar Sesión</Text>

        <View style={styles.form}>
          <Text style={styles.label}>Correo Electrónico</Text>
          <TextInput
            style={styles.input}
            placeholder="ejemplo@email.com"
            value={email}
            onChangeText={setEmail}
            autoCapitalize="none"
            keyboardType="email-address"
            editable={!loading}
          />

          <Text style={styles.label}>Contraseña</Text>
          <TextInput
            style={styles.input}
            placeholder="Ingresa tu contraseña"
            value={password}
            onChangeText={setPassword}
            secureTextEntry
            editable={!loading}
          />

          <TouchableOpacity
            style={styles.loginButton}
            onPress={handleLogin}
            disabled={loading}
          >
            {loading ? (
              <ActivityIndicator color="#FFFFFF" />
            ) : (
              <Text style={styles.loginButtonText}>Ingresar</Text>
            )}
          </TouchableOpacity>
        </View>

        <View style={styles.demoUsers}>
          <Text style={styles.demoTitle}>Usuarios de prueba:</Text>
          {usuariosDemo.map((user, index) => (
            <TouchableOpacity
              key={index}
              style={styles.demoUserItem}
              onPress={() => setEmail(user.email)}
            >
              <Text style={styles.demoUserEmail}>{user.email}</Text>
              <Text style={styles.demoUserName}>👤 {user.name}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F9FF',
  },
  content: {
    flex: 1,
    padding: 24,
    justifyContent: 'center',
  },
  logo: {
    fontSize: 60,
    textAlign: 'center',
  },
  title: {
    fontSize: 36,
    fontWeight: 'bold',
    color: '#0057B8',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 20,
    color: '#172033',
    textAlign: 'center',
    marginBottom: 30,
  },
  form: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 20,
    shadowColor: '#000',
    shadowOpacity: 0.08,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 8,
    elevation: 3,
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    color: '#374151',
    marginBottom: 6,
  },
  input: {
    borderWidth: 1,
    borderColor: '#D1D5DB',
    borderRadius: 10,
    padding: 14,
    fontSize: 16,
    backgroundColor: '#FFFFFF',
    marginBottom: 16,
  },
  loginButton: {
    backgroundColor: '#0057B8',
    borderRadius: 12,
    paddingVertical: 16,
    alignItems: 'center',
    marginTop: 8,
  },
  loginButtonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  demoUsers: {
    marginTop: 24,
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 16,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 2,
  },
  demoTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#172033',
    marginBottom: 10,
  },
  demoUserItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#F3F4F6',
  },
  demoUserEmail: {
    fontSize: 13,
    color: '#0057B8',
  },
  demoUserName: {
    fontSize: 13,
    color: '#526075',
  },
});