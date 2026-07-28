# Demo Package

Bu paket, NovaVision AI platformu konfigürasyon standartlarına ve **Package Model Şartnamesine (XML Specification)** %100 uyumlu olarak oluşturulmuş bir "Demo" paketidir.

## Özellikler (Gereksinimler)

1. **İki Adet Executor İçerir**:
   - `ExecutorOne`: 1 adet girdi (Input) alır, 1 adet çıktı (Output) üretir.
   - `ExecutorTwo`: 2 adet girdi alır, 2 adet çıktı üretir.
2. **Bağımlı Açılır Menü (dependentDropdown)**:
   - Her iki Executor'ın yapılandırma modelinde `DemoDependentDropdown` adlı bir `dependentDropdownlist` alanı bulunur.
   - Bu menünün **OptionA (Method A)** ve **OptionB (Method B)** olmak üzere 2 farklı seçeneği vardır.
   - **OptionA** seçildiğinde, biri `Integer (number)`, diğeri `Boolean (checkbox)` olan iki farklı veri tipinde alan açılır.
   - **OptionB** seçildiğinde, biri `Float (number)`, diğeri `String (textInput)` olan iki farklı veri tipinde alan açılır.

## Görüntü İşleme Yetenekleri (OpenCV)

Bu paket yalnızca mimari kuralları sağlamakla kalmaz, aynı zamanda `cv2` (OpenCV) kütüphanesi ile gerçek görüntü işleme algoritmaları barındırır:
- **ExecutorOne**: Sisteme yüklenen resmi alır ve Siyah-Beyaz (Grayscale) formata çevirerek tek bir çıktı üretir.
- **ExecutorTwo**: Sisteme yüklenen iki farklı resmi alır. Birinci çıktı olarak bu iki resmi harmanlar (Alpha Blending). İkinci çıktı olarak ise iki resim arasındaki piksel farklarını (Absolute Difference) hesaplar.

## Kurulum ve Sistem Gereksinimleri

Bu paketin modül yollarını (import) ve bağımlılıklarını doğru şekilde çözümleyebilmesi için çalışma ortamınıza kurulması gerekmektedir.

- **Python Sürümü**: Pydantic modellerinde kullanılan `Literal` tiplerinin ve güncel konfigürasyon standartlarının desteklenmesi için **Python 3.8 veya üzeri** gereklidir.
- **Kurulum**: Paketin bulunduğu ana dizinde aşağıdaki komutu çalıştırarak projeyi "editable" (düzenlenebilir) modda kurabilirsiniz:
  ```bash
  pip install -e .
  ```
  *Bu işlem `setup.py` dosyasını okuyarak `pydantic`, `opencv-python-headless` gibi gereksinimleri kuracak ve paketi `novavision.demo_package` olarak ortama tanıtacaktır.*

## Dosya Yapısı

- `src/models/PackageModel.py`: Pydantic kullanılarak tanımlanmış olan ve XML Şartnamesine (Literal kuralları, schema_extra hedefleri) tam uyumlu yapılandırma şeması.
- `src/executors/ExecutorOne.py`: 1 Girdi / 1 Çıktı çalışan, Siyah-Beyaz filtre uygulayan birinci işlemci.
- `src/executors/ExecutorTwo.py`: 2 Girdi / 2 Çıktı çalışan, resim harmanlama ve fark bulma işlemleri yapan ikinci işlemci.

*Bu depo eğitim amacıyla oluşturulmuştur.*
